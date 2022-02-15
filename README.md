# Face-Mask-Detection
<p>Face Mask Detection API powered by FastAPI.</p>

- Detects Multiple Faces from afar.
- Classify faces as Mask or No Mask.
- Sends Annotated response of an image with labelled faces.
- Sends Numbers of faces in Headers Response.
- Sends Labels as an array in Header Response.

---

## API
- Made with FASTAPI
- Validation by PyDantic

## Working
- URL: /image
- Type: Post
- Body: form-data
    - Key: "Image"
    - Value: Selected Image

    ### Response
    - Status: 201
        - Annotated Image
    - Headers:
        - "human-count": Number of faces detected
        - "labels": Labels of faces detected [MASK | NO MASK]
