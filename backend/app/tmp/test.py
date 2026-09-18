from app.database.connection import client


async def test_connection():
    try:
        result = await client.admin.command("ping")
        print("MongoDB connection successful!")
        print(result)
    except Exception as e:
        print("MongoDB connection failed!")
        print(e)
    finally:
        await client.close()