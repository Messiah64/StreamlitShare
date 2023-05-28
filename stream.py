import streamlit as st
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer


class MyTransformer(VideoTransformerBase):
    def transform(self, frame):
        # Apply transformations to the frame (e.g., image processing)
        # and return the transformed frame
        return frame


def main():
    st.title("Streamlit WebRTC Example")
    
    webrtc_ctx = webrtc_streamer(
        key="example",
        video_transformer_factory=MyTransformer,
        async_transform=True,
    )
    
    if webrtc_ctx.video_transformer:
        # Display the transformed video frame
        transformed_frame = webrtc_ctx.video_transformer.transformed_frame.to_ndarray()
        st.image(transformed_frame, channels="BGR")


if __name__ == "__main__":
    main()
