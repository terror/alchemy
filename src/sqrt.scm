; newton's sqrt(x) method
; 1. make a guess
; 2. average that guess x/guess
; 3. repeat until the result is good enough

(define (sqrt-iter g x)
  (if (good g x)
    g
    (sqrt-iter (improve g x) x)))

(define (improve g x)
  (avg g (/ x g)))

(define (avg x y) (/ (+ x y) 2))

(define (good g x)
  (< (abs (- (square g) x)) 0.001))

(define (sqrt x)
  (sqrt-iter 1.0 x))

(display (sqrt 100)) (newline)
(display (sqrt 25)) (newline)
(display (sqrt 64)) (newline)

#|

"Sqrt-iter, on the other hand, demonstrates how iteration can be accomplished using no special construct other than the ordinary ability to call a procedure."

|#
