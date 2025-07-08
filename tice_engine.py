def compute_lambda(delta_psi_squared, tau, eta):
    if eta == 0:
        eta = 1e-8
    raw_lambda = (delta_psi_squared * tau) / eta
    scaled_lambda = min(int(raw_lambda * 100), 10000)
    return scaled_lambda