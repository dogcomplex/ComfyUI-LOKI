import os
import json
import subprocess
from pathlib import Path
from datetime import datetime

def ensure_workflow_dir(workflow_name):
    """Create workflow directory if it doesn't exist"""
    base_dir = Path(__file__).parent
    workflow_dir = base_dir / "workflows" / workflow_name
    workflow_dir.mkdir(parents=True, exist_ok=True)
    return workflow_dir

def load_workflow_requests():
    """Load workflow requests from JSON file"""
    base_dir = Path(__file__).parent
    with open(base_dir / "workflow_requests.json", "r") as f:
        return json.load(f)

def load_workflow_info(workflow_dir):
    """Load workflow.json if it exists"""
    workflow_file = workflow_dir / "workflow.json"
    if workflow_file.exists():
        with open(workflow_file, "r") as f:
            return json.load(f)
    return {"status": "pending"}

def save_workflow_info(workflow_dir, info):
    """Save workflow.json"""
    workflow_file = workflow_dir / "workflow.json"
    with open(workflow_file, "w") as f:
        json.dump(info, f, indent=2)

def process_workflow(workflow_name, workflow_data):
    """Process a single workflow"""
    base_dir = Path(__file__).parent
    workflow_dir = ensure_workflow_dir(workflow_name)
    
    # Check if workflow is already completed
    workflow_info = load_workflow_info(workflow_dir)
    if workflow_info.get("status") == "completed":
        print(f"[SKIP] {workflow_name} (already completed)")
        return
    
    print(f"\n[START] Processing {workflow_name}")
    print(f"Description: {workflow_data.get('description', '')}")
    
    try:
        # Initialize workflow info
        workflow_info.update({
            "name": workflow_name,
            "data": workflow_data,
            "description": workflow_data.get("description", ""),
            "requirements": workflow_data.get("requirements", []),
            "status": "processing",
            "timestamp": datetime.now().isoformat()
        })
        save_workflow_info(workflow_dir, workflow_info)
        
        print(f"[RUN] Filtering nodes for {workflow_name}...")
        
        # Run filter_nodes.py with real-time output
        process = subprocess.Popen([
            "python", 
            str(base_dir / "filter_nodes.py"),
            "--prompt", workflow_data["description"],
            "--output-folder", str(workflow_dir)
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)
        
        # Print output in real-time
        while True:
            output = process.stdout.readline()
            if output:
                print(output.rstrip())
            if process.poll() is not None:
                break
            
        # Get final return code
        return_code = process.wait()
        
        if return_code == 0:
            workflow_info.update({
                "status": "completed",
                "output_files": {
                    "installed_nodes": "installed_nodes_filtered.md",
                    "available_nodes": "available_nodes_filtered.md"
                }
            })
            print(f"[DONE] {workflow_name} completed successfully")
        else:
            stderr = process.stderr.read()
            raise subprocess.CalledProcessError(return_code, process.args, stderr=stderr)
            
        save_workflow_info(workflow_dir, workflow_info)
        
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] {workflow_name} failed:")
        print(f"  stderr: {e.stderr}")
        workflow_info.update({
            "status": "error",
            "error": {
                "message": str(e),
                "stderr": e.stderr
            }
        })
        save_workflow_info(workflow_dir, workflow_info)

def main():
    """Main execution function"""
    # Ensure base workflows directory exists
    base_dir = Path(__file__).parent
    (base_dir / "workflows").mkdir(exist_ok=True)
    
    # Load workflow requests
    workflow_requests = load_workflow_requests()
    
    # Process each workflow
    for workflow_name, workflow_data in workflow_requests.items():
        process_workflow(workflow_name, workflow_data)

if __name__ == "__main__":
    main() 