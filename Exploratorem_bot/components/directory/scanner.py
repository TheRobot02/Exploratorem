#thirt-party import
import os

#build-in import

#local import

class scanDirectory:
    async def scan_directory(ctx,path):
        if os.path.isdir(path):
            print(f"Scanning directory: {path}")
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                if os.path.isdir(item_path):
                    await ctx.send(f"Directory: {item}")
                else:
                    await ctx.send(f"File: {item}")
        else:
            await ctx.send(f"{path} is not a directory.")