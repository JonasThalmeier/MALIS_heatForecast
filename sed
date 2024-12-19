stacked_features_train = v.stack(location=("latitude", "longitude"))
flattened_features_train = stacked_features_train.to_array(dim="variables").stack(features=("variables", "feature_dim")).transpose("day", "location", "features")
# Reshape into (rows, features) where rows = day × location
X_train = flattened_features_train.values.reshape(flattened_features_train.shape[0] * flattened_features_train.shape[1], -1)

# Check the resulting shape
print("Shape of flattened features (X_train):", X_train.shape)

flattened_labels_train = train_labels.stack(location=("latitude", "longitude"))
aligned_labels_train = flattened_labels_train.sel(day=stacked_features["day"])
y_train = aligned_labels_train.values.flatten()  # Flatten into a single column
print("Shape of flattened labels (y):", y.shape)
