async function optimizeProduct() {

    const productId = document.getElementById("productId").value.trim();
    const productName = document.getElementById("productName").value.trim();
    const pickFrequency = document.getElementById("pickFrequency").value;
    const quantity = document.getElementById("quantity").value;
    const weight = document.getElementById("weight").value;
    const currentSlot = document.getElementById("currentSlot").value.trim();

    // Validate input
    if (
        productId === "" ||
        productName === "" ||
        pickFrequency === "" ||
        quantity === "" ||
        weight === "" ||
        currentSlot === ""
    ) {
        alert("Please fill in all fields.");
        return;
    }

    const product = {
        product_id: productId,
        product_name: productName,
        pick_frequency: Number(pickFrequency),
        quantity: Number(quantity),
        weight: Number(weight),
        current_slot: currentSlot
    };

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/api/optimize",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    products: [product]
                })
            }
        );

        if (!response.ok) {
            throw new Error(
                "Backend returned status " + response.status
            );
        }

        const data = await response.json();

        console.log("Backend response:", data);

        if (data.status !== "success") {
            alert(data.message || "Optimization failed.");
            return;
        }

        if (
            !data.optimized_products ||
            data.optimized_products.length === 0
        ) {
            alert("No optimization result received.");
            return;
        }

        const result = data.optimized_products[0];

        console.log("Optimization result:", result);


        // PRODUCT
        document.getElementById("resultProduct").textContent =
            result.product_name || productName;


        // MOVEMENT TYPE
        document.getElementById("resultMovement").textContent =
            result.movement || "Unknown";


        // CURRENT SLOT
        document.getElementById("resultCurrentSlot").textContent =
            result.current_slot || currentSlot;


        // RECOMMENDED SLOT
        document.getElementById("resultSlot").textContent =
            result.recommended_slot || "Not assigned";


        // RECOMMENDED ZONE
        document.getElementById("resultZone").textContent =
            result.recommended_zone
                ? "Zone " + result.recommended_zone
                : "Not assigned";


        // OPTIMIZATION SCORE
        const score =
            result.optimization_score ??
            result.score ??
            result.optimizationScore;

        document.getElementById("resultScore").textContent =
            score !== undefined && score !== null
                ? score + "%"
                : "N/A";


        // Scroll to results
        document.getElementById("resultSection").scrollIntoView({
            behavior: "smooth"
        });

    } catch (error) {

        console.error("Optimization error:", error);

        alert(
            "Could not connect to the backend.\n\n" +
            "Make sure Flask is running on port 5000."
        );
    }
}