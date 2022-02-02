; absolute value procedure

(define (abs x)
  (cond
    ((>= x 0) x)
    ((< x 0) (- x))))

(begin
  (newline)
  (display (abs -25))
  (newline))

(begin
  (display (abs 25))
  (newline))
