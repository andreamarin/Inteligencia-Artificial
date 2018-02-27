(setq abierto nil)
(setq cerrado nil)

(defun string-to-list (str)
  (if (not (streamp str))
    (string-to-list (make-string-input-stream str))
      (if (listen str)
        (cons (read str) (string-to-list str))
    nil)
  )
)

(setq in (open "assets/in.txt"))
(setq start (read-line in nil))
(setq end (read-line in nil))
(setq dist (read-line in nil))
(close in)

(setq dist (car(string-to-list dist)))

(setq in (open "assets/connections5.txt"))
(setq neigh (read-line in))
(close in)

(setq neigh (car (string-to-list neigh)))

(defun expand (n h)
  (loop for ls in (cdr (nth n neigh)) do 
    (push (list (car ls) n (+ h (cadr ls)) (cadr (nth (car ls) dist))) abierto)
  )
)

;(defun next ()
