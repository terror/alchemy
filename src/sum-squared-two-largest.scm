; a procedure that takes three numbers as input
; and returns the sum of the square of the two largest numbers

(define (sum-squared-two-largest x y z)
  (let ((mx (max x y z)) (mn (min x y z)))
  (+ (* mx mx) (* (- (+ x y z) mx mn) (- (+ x y z) mx mn)))))

(display (sum-squared-two-largest 2 3 4)) (newline) ; 3^2 + 4^2 => 9 + 16 => 25
