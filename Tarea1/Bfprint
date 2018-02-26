;; Imprimir un árbol por niveles

(defun niveles(tree)
(when (and (listp tree) (not (null tree)))(print (remove-if #'listp tree))(niveles (apply #'append (remove-if #'atom tree)))))
