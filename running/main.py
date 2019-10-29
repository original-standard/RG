


class coeff:
 B_0 = 0
 B_1 = 0
 B_2 = 0
 B_3 = 0
 G_1 = 0
 G_2 = 0
 G_3 = 0
 Z_3 = 1.202
 def __init__(self,N):
  self.B_0 = (11. - 2. * N / 3.)
  self.B_1 = (102. - 38. * N / 3.)
  self.B_2 = (2857. / 2. - 5033. / 18. * N + 325. / 54 * N * N)
  self.B_3 = (149753. / 6. + 3564. * self.Z_3 + (-1078361. / 162. - 6508. / 27. * self.Z_3) * N + (50065. / 162. + 6472. / 81. * self.Z_3) * N * N + 1093. / 729. * N * N * N)
 def Cm1(self):
  pass
 def C0(self):
  pass
 def C1(self):
  pass
 def C2(self):
  pass
 def C0_2(self):
  pass
 def C1_2(self):
  pass
 def C2_2(self):
  pass

class tensor(coeff):
 def __init__(self,N):
  super(tensor, self).__init__(N)
  self.G_1 = 4. / 3.
  self.G_2 = 2. / 27. * (543. - N * 26.)
  self.G_3 = 2. / 243. * (157665. / 2. - 4176. * self.Z_3 - N * (2160. * self.Z_3 + 7860.) -54. * N * N)

 def Cm1(self):
  return 1. / self.B_0
 def C0(self):
  return 1. / self.B_0 * self.B_1 / self.B_0
 def C1(self):
  return 1. / self.B_0 * (self.B_2 / self.B_0 - (self.B_1 / self.B_0) * (self.B_1 / self.B_0))
 def C2(self):
  return 1. / self.B_0 * ((self.B_3 / self.B_0) / 2. - self.B_1 * self.B_2 / self.B_0 / self.B_0 +  (self.B_1 / self.B_0) * (self.B_1 / self.B_0) * (self.B_1 / self.B_0) / 2.)
 def C0_2(self):
  return self.G_1 / self.B_0
 def C1_2(self):
  return (self.G_2 / self.B_0 - self.G_1 / self.B_0 / self.B_0 * self.B_1)
 def C2_2(self):
  return ((self.G_3 - self.G_2 * self.B_1 / self.B_0 - self.G_1 * self.B_2 / self.B_0 + self.G_1 * self.B_1 * self.B_1  / self.B_0 / self.B_0) / 2. / self.B_0)

class scalar(coeff):
 def __init__(self,N):
  super(scalar, self).__init__(N)
  CF = 4. / 9.
  n = N / 6.
  self.G_1 = -1.  * 4.
  self.G_2 = -3.79167 * 4. * 4.
  self.G_3 = -12.4202 * 4. * 4. * 4.

 def Cm1(self):
  return 1. / self.B_0
 def C0(self):
  return 1. / self.B_0 * self.B_1 / self.B_0
 def C1(self):
  return 1. / self.B_0 * (self.B_2 / self.B_0 - (self.B_1 / self.B_0) * (self.B_1 / self.B_0))
 def C2(self):
  return 1. / self.B_0 * ((self.B_3 / self.B_0) / 2. - self.B_1 * self.B_2 / self.B_0 / self.B_0 +  (self.B_1 / self.B_0) * (self.B_1 / self.B_0) * (self.B_1 / self.B_0) / 2.)
 def C0_2(self):
  return self.G_1 / self.B_0
 def C1_2(self):
  return (self.G_2 / self.B_0 - self.G_1 / self.B_0 / self.B_0 * self.B_1)
 def C2_2(self):
  return ((self.G_3 - self.G_2 * self.B_1 / self.B_0 - self.G_1 * self.B_2 / self.B_0 + self.G_1 * self.B_1 * self.B_1  / self.B_0 / self.B_0) / 2. / self.B_0)



