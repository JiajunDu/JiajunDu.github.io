"""
exchange left angle brackets to '&lt;',
and exchange right angle brackets to '&gt;'
"""

left_angle, right_angle = "<", ">"
left_angle_proxy, right_angle_proxy = "&lt;", "&gt;"

input_code = """

"""

def worker(s: str) -> str:
    r1 = s.replace(left_angle, left_angle_proxy)
    r2 = r1.replace(right_angle, right_angle_proxy)
    r3 = r2.strip()
    return "<pre><code lang=\"rust\">" + r3 + "</code></pre>"

print(worker(input_code))