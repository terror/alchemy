(load "lib/test.scm")

; a procedure that returns the sum of elements in `lst`

(define (sum lst)
  (cond ((null? lst) 0)
        (else (+ (car lst) (sum (cdr lst))))))

(define (test)
  (assert-equal (sum '(1 2 3)) 6)
  (assert-equal (sum '(1 2 3 4 5 6)) 21)
  (assert-equal (sum '(185 250 350)) 785)
  (assert-equal (sum '(0 0 0)) 0)
  (display "All tests passed!") (newline))

(test)
