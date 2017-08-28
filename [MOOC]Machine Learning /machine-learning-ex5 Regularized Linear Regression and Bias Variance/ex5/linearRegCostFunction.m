function [J, grad] = linearRegCostFunction(X, y, theta, lambda)
%LINEARREGCOSTFUNCTION Compute cost and gradient for regularized linear 
%regression with multiple variables
%   [J, grad] = LINEARREGCOSTFUNCTION(X, y, theta, lambda) computes the 
%   cost of using theta as the parameter for linear regression to fit the 
%   data points in X and y. Returns the cost in J and the gradient in grad

% Initialize some useful values
m = length(y); % number of training examples

grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost and gradient of regularized linear 
%               regression for a particular choice of theta.
%
%               You should set J to the cost and grad to the gradient.
%


H = X*theta;
J = 1./2./m*(H-y)'*(H-y) + lambda/2/m*theta(2:end)'*theta(2:end);


% =========================================================================
grad = grad(:);
grad(1) = 1./m*(H-y)'*X(:,1);
for i=2:size(theta,1)
    grad(i) = 1./m*(H-y)'*X(:,i) + lambda/m*theta(i);
end
%%grad(2:end) = 1./m*(H-y)'*X(:,2:end) + lambda/m*theta(2:end);


end
