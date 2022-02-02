(load "lib/test.scm")

; a procedure that sums up all digits in a number

; Ex:
; input:  450
; output: 9 (4 + 5 + 0)

(define (sum-digits n)
  (cond ((< n 10) n)
    (else (+ (remainder n 10) (sum-digits (floor (/ n 10))) ))))

; --- tests --

(define (test-sum-digits)
  (assert-equal (sum-digits 40) 4)
  (assert-equal (sum-digits 450) 9)
  (assert-equal (sum-digits 324234) 18)
  (assert-equal (sum-digits 0) 0)
  (assert-equal (sum-digits 0123) 6))

; --- main ---

(define (main)
  (test-sum-digits)
  (display "All tests passed!") (newline))

(main)
