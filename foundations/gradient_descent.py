class Solution:
    def get_val(self, x):
        return x*x

    def new_val(self, x, alpha):
        return x - alpha * 2 * x
    
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        x = init
        for _ in range(iterations):
            x = self.new_val(x,learning_rate)

        return round(x,5)
         


