from fastapi import APIRouter, UploadFile, File, Form, HTTPException
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
router = APIRouter()
chat_sessions = {}

def get_chat_session(session_id: str = "default"):
    """Retrieves or initializes a chat session for contextual memory."""
    if session_id not in chat_sessions:
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise HTTPException(status_code=500, detail="API Key is missing from .env")

        genai.configure(api_key=api_key)

        try:
            model = genai.GenerativeModel(
                model_name='gemini-flash-latest',
            )
            chat_sessions[session_id] = model.start_chat(history=[])
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Model initialization failed: {str(e)}")

    return chat_sessions[session_id]

@router.post("/analyze")
async def analyze_task(
    message: str = Form(...),
    file: UploadFile = File(None)
):
    """Processes multimodal input (text + image) and returns AI-generated solutions."""
    try:
        chat = get_chat_session()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    content = []
    if file:
        img_data = await file.read()
        content.append({
            "mime_type": file.content_type or "image/png",
            "data": img_data
        })
    
    enhanced_prompt = f"If needed, use Google Search to find the most up-to-date information for this request: {message}"
    content.append(enhanced_prompt)

    try:
        response = chat.send_message(content)
        return {
            "description": message,
            "solution": response.text
        }
    except Exception as e:
        global chat_sessions
        if "default" in chat_sessions:
            del chat_sessions["default"]
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

@router.get("/reset")
async def reset_memory():
    """Wipes the active chat memory."""
    global chat_sessions
    chat_sessions = {}
    return {"status": "Memory successfully cleared."}