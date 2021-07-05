; factorial

(define (fact n)
  (if (= n 1)
    1
    (* n (fact (- n 1)))))

(define (fact-iter p c m)
  (if (> c m)
    p
    (fact-iter (* c p) (+ c 1) m)))

(display (fact 6)) (newline)
(display (fact-iter 1 1 6)) (newline)
