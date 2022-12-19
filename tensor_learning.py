# # import torch

# # shape = (2, 3,)
# # other_shape = (2,3)

# # rand_tensor = torch.rand(shape)
# # rand_tensor2 = torch.rand(*other_shape)
# # print(rand_tensor.shape,rand_tensor2.shape)
# # ones_tensor = torch.ones(shape)
# # zeros_tensor = torch.zeros(shape)

# # print(f"Random Tensor: \n {rand_tensor} \n")
# # print(f"Ones Tensor: \n {ones_tensor} \n")
# # print(f"Zeros Tensor: \n {zeros_tensor}")

# # a = torch.tensor([2., 3.], requires_grad=True)
# # b = torch.tensor([6., 4.], requires_grad=True)

# # Q = 3*a**3 - b**2
# # print(Q)
# # Q.backward(gradient=torch.ones_like(Q))
# # print(a.grad,b.grad)