(load "lib/test.scm")

; a recursive procedure
; that counts how many occurences of `item` are in `lst`
; car -> first, cdr -> rest

(define (count lst item)
  (cond ((null? lst) 0)
    ((= (car lst) item) (+ 1 (count (cdr lst) item)))
    (else (count (cdr lst) item)) ))

(define (test)
  (assert-equal (count '(1 2 3) 1) 1)
  (assert-equal (count '(1 1 1 1 1) 1) 5)
  (assert-equal (count '(1 0 1 0 1) 2) 0)
  (display "All tests passed!") (newline))

(test)
