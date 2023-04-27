import numpy as np
def svd_solver(A,mask,t=None,delta=None,epsilon=1e-3,max_iterations=1000):
  Y=np.zeros_like(A)

  #initialize the step
  if not t:
    t=5*np.sum(A.shape)/2
  if not delta:
    delta=1.2*np.prod(A.shape)/np.sum(mask)

  for i in range(max_iterations):
    #SVD decomposition
    U,S,V=np.linalg.svd(Y,full_matrices=False)
    #soft-thresholding operator
    S=np.maximum(S-t,0)
    #singular value shrinkage
    X=np.linalg.multi_dot([U,np.diag(S),V])
    #interation of Y
    Y+=delta*mask*(A-X)
    #error calculation
    error=np.linalg.norm(mask*(X-A))/np.linalg.norm(mask*A)
    if error<epsilon:
      break
  return X