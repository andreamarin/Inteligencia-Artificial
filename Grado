
;;Obtener el grado de un árbol (máximo número de hijos)

(defun grado (tree)
(cond
((atom tree) 0)
(t (apply #'max (count-if #'atom tree) (mapcar #'grado tree))))
