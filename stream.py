import streamlit as st
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer


class MyTransformer(VideoTransformerBase):
    def transform(self, frame):
        # Apply transformations to the frame (e.g., image processing)
        transformed_frame = frame.to_ndarray(format="bgr24")
        
        # Display the transformed frame
        st.image(transformed_frame, channels="BGR")
        
        # Return the original frame
        return frame


def main():
    st.title("Streamlit WebRTC Example")
    
    webrtc_ctx = webrtc_streamer(
        key="example",
        video_transformer_factory=MyTransformer,
        async_transform=True,
    )


if __name__ == "__main__":
    main()
