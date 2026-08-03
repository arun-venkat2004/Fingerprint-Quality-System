from quality import (
    read_image,
    check_blur,
    check_brightness,
    check_contrast,
    check_noise,
    overall_score
)

import streamlit as st

st.set_page_config(
    page_title="Fingerprint Quality Assessment",
    layout="centered"
)

st.title("🖐️ Fingerprint Quality Assessment System")

st.write("Welcome to the Fingerprint Quality Assessment Project")

uploaded_file = st.file_uploader(
    "Upload Fingerprint Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    st.success("✅ Image Uploaded Successfully")

    image = read_image(uploaded_file)

    st.image(
        image,
        channels="BGR",
        caption="Uploaded Fingerprint",
        use_container_width=True
    )

    # --------------------------
    # Blur
    # --------------------------

    blur_score = check_blur(image)

    st.write(f"## Blur Score : {blur_score:.2f}")

    if blur_score > 150:
        st.success("✅ Good Quality Image")
    else:
        st.error("❌ Blurry Image")

    # --------------------------
    # Brightness
    # --------------------------

    brightness = check_brightness(image)

    st.write(f"## Brightness : {brightness:.2f}")

    if brightness < 80:
        st.warning("🌙 Too Dark")

    elif brightness > 180:
        st.warning("☀️ Too Bright")

    else:
        st.success("✅ Good Brightness")

    # --------------------------
    # Contrast
    # --------------------------

    contrast = check_contrast(image)

    st.write(f"## Contrast : {contrast:.2f}")

    if contrast > 50:
        st.success("✅ Good Contrast")

    else:
        st.warning("⚠️ Low Contrast")

    # --------------------------
    # Noise
    # --------------------------

    noise = check_noise(image)

    st.write(f"## Noise : {noise:.2f}")

    if noise < 8:
        st.success("✅ Low Noise")

    elif noise < 15:
        st.warning("⚠️ Medium Noise")

    else:
        st.error("❌ High Noise")

    # --------------------------
    # Overall Score
    # --------------------------

    score, status = overall_score(
        blur_score,
        brightness,
        contrast,
        noise
    )

    st.divider()

    st.subheader("📊 Overall Fingerprint Quality")

    st.metric(
        label="Quality Score",
        value=f"{score}%"
    )

    if score >= 90:
        st.success(status)

    elif score >= 75:
        st.success(status)

    elif score >= 50:
        st.warning(status)

    else:
        st.error(status)