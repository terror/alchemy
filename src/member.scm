(load "lib/test.scm")

; writing a member? procedure

; returns a bool
; #t  => item is a member of list
; #f  => item is not a member of list

(define (member? lst item)
  (cond ((null? lst) #f)
    ((= item (car lst)) #t)
    (else (member? (cdr lst) item)) ))

; --- tests ---

(define (test-member?)
  (assert-equal (member? '(1 2 3) 1) #t)
  (assert-equal (member? '(1 2 3) 4) #f)
  (assert-equal (member? '() 10) #f)
  (assert-equal (member? '(1 2 3 4 9 8 9 0 0 8 8 7) 7) #t))

; main

(define (main)
  (test-member?)
  (display "All tests passed!")
  (newline))

(main)
