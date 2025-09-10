import pandas as pd

# Step 1: Get all dataviews
dataviews = cja.getDataViews()
dv_map = dict(zip(dataviews["id"], dataviews["name"]))

# --- Helper function to build a shared components matrix ---
def build_shared_matrix(fetch_fn, comp_type):
    results = {}
    id_to_name = {}

    for dv_id, dv_name in dv_map.items():
        try:
            comps = fetch_fn(dv_id, inclType=True, full=True)
            shared = comps[comps["sharedComponent"] == True][["id", "name"]]

            results[dv_name] = set(shared["id"].tolist())
            id_to_name.update(dict(zip(shared["id"], shared["name"])))
        except Exception as e:
            print(f"Error fetching {comp_type} for {dv_id} ({dv_name}): {e}")

    all_ids = sorted(set().union(*results.values()))
    df = pd.DataFrame(index=all_ids)

    for dv_name, comp_ids in results.items():
        df[dv_name] = df.index.isin(comp_ids).astype(int)

    df.insert(0, "name", df.index.map(id_to_name))
    df.insert(0, "type", comp_type)   # add dimension/metric tag
    return df

# Step 2: Build and tag both
dims_df = build_shared_matrix(cja.getDimensions, "dimension")
metrics_df = build_shared_matrix(cja.getMetrics, "metric")

# Step 3: Combine into one DataFrame
combined_df = pd.concat([dims_df, metrics_df])

# Step 4: Save to CSV in your folder
output_path = "{enter your path}/shared_components_matrix.csv"
combined_df.to_csv(output_path, index_label="id")

print(f"? Combined CSV written to: {output_path}")

# Display preview
display(combined_df.head())
