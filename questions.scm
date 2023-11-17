(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
    ; BEGIN PROBLEM 15
    ; (define (len-helper s i)
    ;     (if (null? (cdr s))
    ;         i
    ;         (len-helper (cdr s) (+ i 1))
    ;     )
    ; )
    (define (enumerate-helper s i)
        (if (null? s)
            ()
            (if (null? (cdr s))
                ; (list i (car s))
                ; (list (list i (car s)) (enumerate-helper (cdr s) (+ i 1)))

                ; (cons i_reverse (car s))
                ; (enumerate-helper s (- i_reverse 1)

                (cons (list i (car s)) nil)
                (cons (list i (car s)) (enumerate-helper (cdr s) (+ i 1)))
                ; (if (zero? i)
                ;     (cons (list (car s) i) (cons (enumerate-helper (cdr s) (+ i 1))))
                ;     (list (car s) i) (cons (enumerate-helper (cdr s) (+ i 1)))
                    ; (list (car s) i) (cons `(,enumerate-helper ,(cdr s) ,(+ i 1)))
                ; )
            )
        )
    )
    ; (define i (len-helper s 0))
    ; i
    (enumerate-helper s 0)
)
    ; END PROBLEM 15

;; Problem 16

;; Merge two lists S1 and S2 according to ORDERED? and return
;; the merged lists.
(define (merge ordered? s1 s2)
  ; BEGIN PROBLEM 16
  'replace-this-line
  )
  ; END PROBLEM 16

;; Optional Problem 2

;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN OPTIONAL PROBLEM 2
         'replace-this-line
         ; END OPTIONAL PROBLEM 2
         )
        ((quoted? expr)
         ; BEGIN OPTIONAL PROBLEM 2
         'replace-this-line
         ; END OPTIONAL PROBLEM 2
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN OPTIONAL PROBLEM 2
           'replace-this-line
           ; END OPTIONAL PROBLEM 2
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN OPTIONAL PROBLEM 2
           'replace-this-line
           ; END OPTIONAL PROBLEM 2
           ))
        (else
         ; BEGIN OPTIONAL PROBLEM 2
         'replace-this-line
         ; END OPTIONAL PROBLEM 2
         )))

; Some utility functions that you may find useful to implement for let-to-lambda

(define (zip pairs)
  'replace-this-line)
