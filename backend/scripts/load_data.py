import pandas as pd
import sys
import os
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

# Add the parent directory to the path to import app modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import engine, SessionLocal
from app.models import Product, Base

def create_tables():
    """Create all tables in the database"""
    Base.metadata.create_all(bind=engine)

def load_products_from_csv(csv_file_path: str):
    """Load products from CSV file into the database"""
    try:
        # Read CSV file
        df = pd.read_csv(csv_file_path)
        
        # Create database session
        db = SessionLocal()
        
        # Clear existing products (optional - remove if you want to append)
        db.query(Product).delete()
        
        # Insert products from CSV
        for _, row in df.iterrows():
            product = Product(
                product_id=row['product_id'],
                product_name=row['product_name'],
                category=row['category'],
                price=row['price'],
                stock_quantity=row['stock_quantity'],
                description=row['description']
            )
            db.add(product)
        
        # Commit changes
        db.commit()
        print(f"Successfully loaded {len(df)} products from {csv_file_path}")
        
    except Exception as e:
        print(f"Error loading data: {e}")
        db.rollback()
    finally:
        db.close()

def main():
    """Main function to set up database and load data"""
    print("Setting up database...")
    create_tables()
    
    # Load products from CSV
    csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")
    if os.path.exists(csv_path):
        print(f"Loading products from {csv_path}")
        load_products_from_csv(csv_path)
    else:
        print(f"CSV file not found at {csv_path}")
        print("Please ensure the products.csv file exists in the data directory")

if __name__ == "__main__":
    main() 