(defun abiertoInsert(obj l)
  (cond
    ((Null l) (cons obj l))
    ((< (last obj) (last (car l))) (cons obj (remove (car obj) l :key 'first)))
    ((= (car obj) (caar l)) l)
    (t (cons (car l) (abiertoInsert obj (cdr l))))
    )
)

(setq in (open "assets/coordenadas.txt")) ;; archivo con las coordenadas 
(setq coordenadas (read-line in))
(close in)

(setq coordenadas (string-to-list coordenadas))

(setq coor-end (cadr(nth end coordenadas)))

(defun contorno(current node)
  (setq (df1 (sqrt (+ (expt (- (second node) (car current)) 2) (expt (- (cadr node) (cadr current)) 2 )))) (df2 (sqrt (+ (expt (- (car node) (car coor-end))  2) (expt (- (cadr node) (cadr coor-end)) 2 )))) )
  (<= (+ df1 df2) (* 2 a)) 
)

(defun expand(node)
  (setq (c ( / (sqrt (+ (expt  (- (third node) (car coor-end)) 2) (expt (fourth node) (cadr coor-end))) 2) 2 )) (a (* (sqrt 2) c)))
  (loop for ls in (cdr nth (car n) neigh) do
	(let coor (nth (car ls) coordenadas))
	(when (contorno (list (third node) (fourth node)) coor) (setq (g (cadr ls)) (h  (+ (sixth node) (cadr (nth (car ls) dist)))) )  (abiertoInsert (list (car ls) (car node) (second coor) (caddr coor) g h (+ g h) ) abierto))
  )
)



(defun backtrackCerrado(son)
  (cond
    ((Null son))
    (t (push son final) (backtrackCerrado (cadr (find son l :key 'first))))
    )
  )

