(define (compose f g)
  (lambda (x) (f (g x))))

(display ((compose car cdr) '(cool stuff))) ; stuff
