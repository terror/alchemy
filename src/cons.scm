; cons

(define (con x y)
  (define (dispatch msg)
    (if (= msg 'l') (x) y))
  dispatch)

(define (pair (con 2 3)))

(begin
  (newline)
  (display (pair 'l'))
  (newline))

(begin
  (display (pair 'r'))
  (newline))
