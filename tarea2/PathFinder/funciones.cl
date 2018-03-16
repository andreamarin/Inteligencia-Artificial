(defun abiertoInsert(obj l)
  (cond
    ((Null l) (cons obj l))
    ((< (last obj) (last (car l))) (cons obj (remove (car obj) l :key 'first)))
    ((= (car obj) (caar l)) l)
    (t (cons (car l) (abiertoInsert obj (cdr l))))
    )
  )

(defun contorno(current node)
  t
  )

(defun backtrackCerrado(son)
  (cond
    ((Null son))
    (t (push son final) (backtrackCerrado (cadr (find son l :key 'first))))
    )
  )

