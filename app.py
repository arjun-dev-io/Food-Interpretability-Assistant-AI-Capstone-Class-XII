import os

import joblib
import pandas as pd
import streamlit as st




BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "nova_classifier.joblib"
)


FEATURES = [
    "energy-kcal_100g",
    "fat_100g",
    "saturated-fat_100g",
    "carbohydrates_100g",
    "sugars_100g",
    "proteins_100g",
    "fiber_100g",
    "sodium_100g"
]


DISPLAY_NAMES = {
    "energy-kcal_100g": "Energy (kcal)",
    "fat_100g": "Fat (g)",
    "saturated-fat_100g": "Saturated fat (g)",
    "carbohydrates_100g": "Carbohydrates (g)",
    "sugars_100g": "Sugars (g)",
    "proteins_100g": "Protein (g)",
    "fiber_100g": "Fiber (g)",
    "sodium_100g": "Sodium (g)"
}


NOVA_LABELS = {
    1: "NOVA 1 — Unprocessed / Minimally Processed",
    2: "NOVA 2 — Processed Culinary Ingredients",
    3: "NOVA 3 — Processed Foods",
    4: "NOVA 4 — Ultra-Processed Foods"
}


NOVA_DESCRIPTIONS = {
    1: (
        "Unprocessed or minimally processed foods. "
        "These are foods that have undergone little processing "
        "and generally retain their original characteristics."
    ),

    2: (
        "Processed culinary ingredients. "
        "These are substances commonly obtained from foods "
        "and used to prepare or season other foods."
    ),

    3: (
        "Processed foods. "
        "These are foods that have been processed from "
        "relatively simple ingredients."
    ),

    4: (
        "Ultra-processed foods. "
        "These are industrial formulations typically made "
        "with multiple ingredients and processing techniques."
    )
}


NOVA_REFERENCE = {
    1: (
        "**NOVA 1 — Unprocessed / Minimally Processed:** "
        "Whole foods like fresh fruits, vegetables, eggs, or milk."
    ),

    2: (
        "**NOVA 2 — Processed Culinary Ingredients:** "
        "Oils, butter, sugar, and salt used in cooking."
    ),

    3: (
        "**NOVA 3 — Processed Foods:** "
        "Simple combinations like canned vegetables, freshly baked bread, or cheese."
    ),

    4: (
        "**NOVA 4 — Ultra-Processed Foods:** "
        "Industrial formulations with additives, preservatives, or artificial flavors "
        "(e.g., chips, sodas, packaged snacks)."
    )
}


CONSUMER_TAKEAWAYS = {
    1: (
        "Suggested Action: Minimal or basic processing. "
        "Excellent choice as part of a wholesome, whole-food diet."
    ),

    2: (
        "Suggested Action: Minimal or basic processing. "
        "Excellent choice as part of a wholesome, whole-food diet."
    ),

    3: (
        "Suggested Action: This product is processed. "
        "It can fit into a balanced diet, but pay attention to "
        "added salt, sugar, or fats."
    ),

    4: (
        "Suggested Action: This product is classified as Ultra-Processed "
        "due to industrial formulation. Consider consuming it in moderation "
        "as an occasional treat rather than a daily staple."
    )
}


st.set_page_config(
    page_title="Food Label Interpretability Assistant",
    page_icon="🥫",
    layout="centered"
)


@st.cache_resource
def load_model():
    model_package = joblib.load(MODEL_PATH)
    return model_package["model"]


try:
    model = load_model()

except Exception as error:
    st.error(
        "The application could not load the trained model."
    )

    st.code(str(error))
    st.stop()


st.title("🥫 Food Label Interpretability Assistant")

st.write(
    "Enter the nutritional information of a packaged food "
    "product to obtain a model-predicted NOVA group and "
    "an explanation of the prediction."
)

st.info(
    "Enter values exactly as reported per 100 g or 100 ml "
    "on the nutrition label."
)


with st.expander("ℹ️ Understanding NOVA Classification"):

    st.write(
        "NOVA is a classification system that groups foods "
        "according to the degree and type of processing they undergo."
    )

    for nova_group in [1, 2, 3, 4]:
        st.write(NOVA_REFERENCE[nova_group])


product_name = st.text_input(
    "Product name",
    placeholder="e.g. 24 mantra peanut"
)


st.subheader("Nutritional information")

col1, col2 = st.columns(2)


with col1:
    energy = st.number_input(
        "Energy (kcal)",
        min_value=0.0,
        max_value=2000.0,
        value=0.0,
        step=0.1
    )

    fat = st.number_input(
        "Fat (g)",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=0.1
    )

    saturated_fat = st.number_input(
        "Saturated fat (g)",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=0.1
    )

    carbohydrates = st.number_input(
        "Carbohydrates (g)",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=0.1
    )


with col2:
    sugars = st.number_input(
        "Sugars (g)",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=0.1
    )

    proteins = st.number_input(
        "Protein (g)",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=0.1
    )

    fiber = st.number_input(
        "Fiber (g)",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=0.1
    )

    sodium = st.number_input(
        "Sodium (g)",
        min_value=0.0,
        max_value=10.0,
        value=0.0,
        step=0.0001,
        format="%.4f"
    )


if st.button(
    "Analyze Product",
    type="primary",
    use_container_width=True
):

    if not product_name.strip():
        st.warning(
            "Please enter a product name."
        )
        st.stop()

    input_data = pd.DataFrame(
        [[
            energy,
            fat,
            saturated_fat,
            carbohydrates,
            sugars,
            proteins,
            fiber,
            sodium
        ]],
        columns=FEATURES
    )

    prediction = model.predict(input_data)[0]

    probabilities = model.predict_proba(input_data)[0]
    classes = model.classes_

    probability_dict = dict(
        zip(classes, probabilities)
    )

    predicted_probability = probability_dict[prediction]

    predicted_label = NOVA_LABELS.get(
        int(prediction),
        f"NOVA {int(prediction)}"
    )

    st.divider()

    st.subheader("Analysis Result")

    st.metric(
        "Model-predicted NOVA Group",
        predicted_label
    )

    st.write(
        f"Model confidence: "
        f"**{predicted_probability * 100:.1f}%**"
    )


    st.subheader("What does this mean?")

    nova_description = NOVA_DESCRIPTIONS.get(
        int(prediction),
        "No description is available for this NOVA group."
    )

    st.write(nova_description)

    st.caption(
        "This is a prediction made by the trained machine-learning "
        "model using nutritional features. It should not be treated "
        "as an official NOVA classification based on the complete "
        "ingredient list or manufacturing process."
    )


    st.subheader("Consumer Takeaway")

    consumer_takeaway = CONSUMER_TAKEAWAYS.get(
        int(prediction),
        "No consumer guidance is available for this prediction."
    )

    if int(prediction) == 4:
        st.warning(consumer_takeaway)

    else:
        st.info(consumer_takeaway)


    st.subheader("Model confidence distribution")

    probability_table = pd.DataFrame({
        "NOVA Group": [
            NOVA_LABELS.get(
                int(c),
                f"NOVA {int(c)}"
            )
            for c in classes
        ],

        "Probability": [
            f"{probability_dict[c] * 100:.1f}%"
            for c in classes
        ]
    })

    st.table(probability_table)


    if hasattr(model, "feature_importances_"):

        with st.expander(
            "View overall model feature importance"
        ):

            st.write(
                "This shows how important each nutritional feature "
                "was to the Random Forest model across its "
                "predictions."
            )

            importance_df = pd.DataFrame({
                "Feature": [
                    DISPLAY_NAMES[f]
                    for f in FEATURES
                ],

                "Importance":
                    model.feature_importances_
            })

            importance_df = importance_df.sort_values(
                "Importance",
                ascending=False
            )

            st.bar_chart(
                importance_df.set_index("Feature")
            )


    st.warning(
        "NOVA classification describes the degree of food "
        "processing rather than overall healthiness. A higher "
        "or lower NOVA group should not by itself be interpreted "
        "as a complete measure of nutritional quality."
    )


    st.success(
        f"Analysis complete for **{product_name.strip()}**."
    )
