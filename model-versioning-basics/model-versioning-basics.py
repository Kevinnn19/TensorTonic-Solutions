from datetime import datetime
def promote_model(models):
    """
    Decide which model version to promote to production.
    """
    # Write code here
    best_model = max(models, key=lambda m: (m["accuracy"], -m["latency"], datetime.fromisoformat(m["timestamp"])))
    return best_model["name"]