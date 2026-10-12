def optimize_products(products):

    results = []

    for product in products:

        product_id = product.get("product_id", "")
        product_name = product.get("product_name", "")
        pick_frequency = float(product.get("pick_frequency", 0))
        quantity = int(product.get("quantity", 0))
        weight = float(product.get("weight", 0))
        current_slot = product.get("current_slot", "")

        # Movement classification
        if pick_frequency >= 70:
            movement = "Fast"
            zone = "A"

        elif pick_frequency >= 40:
            movement = "Medium"
            zone = "B"

        else:
            movement = "Slow"
            zone = "C"

        # Storage level based on weight
        if weight >= 10:
            storage_level = "LOW"

        elif weight >= 5:
            storage_level = "MEDIUM"

        else:
            storage_level = "HIGH"

        # Recommended slot
        recommended_slot = f"{zone}-{storage_level}"

        # Optimization score
        frequency_score = min(pick_frequency, 100)

        if weight <= 5:
            weight_score = 100
        elif weight <= 10:
            weight_score = 80
        else:
            weight_score = 60

        optimization_score = round(
            (frequency_score * 0.7) +
            (weight_score * 0.3),
            1
        )

        results.append({
            "product_id": product_id,
            "product_name": product_name,
            "pick_frequency": pick_frequency,
            "quantity": quantity,
            "weight": weight,
            "current_slot": current_slot,

            "movement": movement,
            "recommended_zone": zone,
            "recommended_slot": recommended_slot,
            "storage_level": storage_level,
            "optimization_score": optimization_score
        })

    return results