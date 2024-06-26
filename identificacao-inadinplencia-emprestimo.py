n = int(input())
matrices = []

for n in range(0, n):
    matrix = input()
    matrices.append(matrix.split(','))
    
def format_float(value):
    formatted_value = f"{value:.2f}"
    if formatted_value[-1] == '0':
        return formatted_value[:-1]
    return formatted_value

# Function to calculate accuracy and precision metrics
def calculate_metrics(matrix):
    tp, fp, fn, tn = map(int, matrix)
    accuracy = (tp + tn) / (tp + fp + fn + tn)
    precision = tp / (tp + fp) if (tp + fp) != 0 else 0
    return accuracy, precision

# Function to find the matrix index with the best combined accuracy and precision
def best_performance(matrices):
    best_index = 0
    best_accuracy = 0
    best_precision = 0
    
    # Loop through each matrix to calculate metrics
    for index, matrix in enumerate(matrices):
        # TODO: Calculate accuracy and precision
        accuracy, precision = calculate_metrics(matrix)

        # Update best metrics if found
        if (accuracy > best_accuracy) or (accuracy == best_accuracy and precision > best_precision):
            best_index = index + 1
            best_accuracy = accuracy
            best_precision = precision

    return best_index, best_accuracy, best_precision

# Find the best performance
index, accuracy, precision = best_performance(matrices)

# Print the results
print(f"Índice: {index}")
print(f"Acurácia: {format_float(accuracy)}")
print(f"Precisão: {format_float(precision)}")