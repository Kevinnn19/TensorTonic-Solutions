def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    # Write code here
    x1a, y1a, x2a, y2a = box_a
    x1b, y1b, x2b, y2b = box_b
    xleft = max(x1a, x1b)
    ytop = max(y1a, y1b)
    xright = min(x2a, x2b)
    ybottom = min(y2a, y2b)
    if xright <= xleft or ytop >= ybottom:
        intersection = 0.0
    else:
        intersection = (xright - xleft) * (ybottom - ytop)
    aarea = (x2a - x1a) * (y2a - y1a)
    barea = (x2b - x1b) * (y2b - y1b)
    union = aarea + barea - intersection
    if union == 0.0:
        return 0.0
    return intersection / union