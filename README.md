1. 可以用 print 在 Stdout 看結果</br>
2. 別宣告太多變數，讓單一變數覆蓋</br>
3. [sliding window](https://www.geeksforgeeks.org/window-sliding-technique/)</br>
4. [Time Complexity of the Built-in Python Functions](https://medium.com/@nedspnt/how-to-make-your-code-run-faster-time-complexity-of-the-built-in-python-functions-38a415008fa2)</br>
5. The easiest way to reduce the time complexity is to avoid a for loop whenever possible.</br>
6. code 太長換行用 \</br>
7. [multiple OR in if statement?](https://stackoverflow.com/questions/17615020/what-is-the-best-approach-in-python-multiple-or-or-in-in-if-statement) : if cond in {'1','2','3','4'}:
8. [Putting a simple if-then-else statement on one line](https://stackoverflow.com/questions/2802726/putting-a-simple-if-then-else-statement-on-one-line) : 'Yes' if fruit == 'Apple' else 'No'</br>
9. [ValueError: Exceeds the limit (4300) for integer string conversion](https://stackoverflow.com/questions/73693104/valueerror-exceeds-the-limit-4300-for-integer-string-conversion) :</br>
   import sys</br>
   sys.set_int_max_str_digits(0)</br>
10. [caret (^) operator](https://stackoverflow.com/questions/2451386/what-does-the-caret-operator-do) : bitwise XOR (exclusive OR)</br>
11. list 用 l = sorted(l) 會比 l.sort() 還快</br>
12. 兩兩相乘的題目，迴圈的終點，可以思考用 int(num**0.5)+1 ex: #492 #507</br>
13. #557 用 list 去處理 for loop 的東西，會比用 string 的處理快</br>
14. 變數後面加底線 : 避免與 python 關鍵字衝突, ex: sum_, class_</br>
15. [How to Break out of multiple loops](https://www.geeksforgeeks.org/how-to-break-out-of-multiple-loops-in-python/?fbclid=IwAR3pOpp323cET1hE3HCNsOWO6sEwOpzrfwQzFpXx4lnzq4L6IN_V9v2OLMQ)
      * 若有多層 loops, break 只會跳出最內層
      * 若要一次跳出整個 loops
         * return
         * else: continue
         * use a flag variable

16.[What is the difference between dict and collections.defaultdict?](https://www.google.com/search?q=difference+between+defaultdict+and+dict&rlz=1C1CHBF_zh-TWTW1031TW1031&oq=&gs_lcrp=EgZjaHJvbWUqDAgBECMYJxjqAhiMBDIMCAAQIxgnGOoCGIwEMgwIARAjGCcY6gIYjAQyDAgCECMYJxjqAhiMBDIMCAMQIxgnGOoCGIwEMgwIBBAjGCcY6gIYjAQyDAgFECMYJxjqAhiMBDIMCAYQIxgnGOoCGIwEMgwIBxAjGCcY6gIYjATSAQgzNjAzajBqOagCCLACAQ&sourceid=chrome&ie=UTF-8): defaultdict will "default" a value if that key has not been set yet</br>
17. 從一串 list 中要找出某個 index 的題目, 可用 enumerate 發想
