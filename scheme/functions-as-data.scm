(load "lib/test.scm")

; functions as data

; sum the squares from a->b
(define (sum-squared a b)
  (if (> a b)
    0
    (+ (* a a) (sum-squared (+ 1 a) b)) ))

; sum the cubes from a->b
(define (sum-cubed a b)
  (if (> a b)
    0
    (+ (* a a a) (sum-cubed (+ 1 a) b)) ))

; goal: generalize the above two methods (they are structurally the same thing!)

(define (sum fn a b)
  (if (> a b)
    0
  (+ (fn a) (sum fn (+ a 1) b)) ))

; --- tests ---

(define (test-sum-squared)
      (assert-equal (sum-squared 3 5) 50)
      (assert-equal (sum-squared 5 3) 0)
      (display "[Sum Squared] All tests passed!") (newline))

(define (test-sum-cubed)
      (assert-equal (sum-cubed 3 5) 216)
      (assert-equal (sum-cubed 5 3) 0)
      (display "[Sum Cubed] All tests passed!") (newline))

(define (test-sum)
      ; define lambdas for square and cubed
      (define a (lambda (x) (* x x)))
      (define b (lambda (x) (* x x x)))

      ; assert
      (assert-equal (sum a 3 5) 50)
      (assert-equal (sum b 3 5) 216)
      (assert-equal (sum a 5 3) 0)
      (assert-equal (sum b 5 3) 0)

      (display "[Sum] All tests passed!") (newline))

; --- main ---

(define (main)
  (test-sum-squared)
  (test-sum-cubed)
  (test-sum))

(main)
