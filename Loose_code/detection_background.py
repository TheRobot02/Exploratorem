#thirt-party import
import asyncio

#build-in import

#local import


from .detection import WebcamDetection

class WebcamDetectionBackgroundProcess:
    async def webcam_detection(ctx):
        detection = WebcamDetection()
        loop = asyncio.get_event_loop()
        user_detected = await loop.run_in_executor(None, detection.start)
        if user_detected == True:
             await ctx.send(f"[+] User has returned!")
        else:
            await ctx.send(f"[!] Error")
