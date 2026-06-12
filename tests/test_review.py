from services.review_service import review_code
from services.comment_formatter import format_comment

diff = """
diff --git a/demo.py b/demo.py
index 3966d60..6ffd368 100644
--- a/demo.py
+++ b/demo.py
@@ -27,4 +27,4 @@ def is_prime(number):
 if is_prime(num)
     print(f"{num} is a prime number!")
 else:
-    print(f"{num} is not a prime number.")
\ No newline at end of file
+    print(f"{num} is not a prime number.)
\ No newline at end of file
"""

review = review_code(diff)

comment = format_comment(review)


print(review)
print(comment)