from django.core.management.base import BaseCommand
import json
from datetime import datetime
from bson import ObjectId
from core.models import Feedback

class Command(BaseCommand):
    help = 'Import feedback data from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file')

    def handle(self, *args, **options):
        file_path = options['json_file']
        
        try:
            # Read JSON file
            with open(file_path, 'r') as file:
                # If your data is a single object, wrap it in a list
                data = json.load(file)
                if isinstance(data, dict):
                    data = [data]
            
            success_count = 0
            error_count = 0
            
            for item in data:
                try:
                    # Convert string _id to ObjectId
                    if '_id' in item:
                        item['_id'] = ObjectId(item['_id'])
                    
                    # Check for existing record
                    if Feedback.objects.filter(id=item['id']).exists():
                        self.stdout.write(
                            self.style.WARNING(f"Feedback {item['id']} already exists, skipping...")
                        )
                        continue
                    
                    # Parse datetime fields
                    for field in ['created_at', 'updated_at']:
                        if item.get(field):
                            item[field] = datetime.fromisoformat(item[field])
                    
                    if 'customer' in item and item['customer']:
                        for field in ['created_at', 'updated_at']:
                            if item['customer'].get(field):
                                item['customer'][field] = datetime.fromisoformat(item['customer'][field])
                    
                    # Create feedback record
                    Feedback.objects.create(**item)
                    success_count += 1
                    self.stdout.write(
                        self.style.SUCCESS(f"Successfully imported feedback {item['id']}")
                    )
                    
                except Exception as e:
                    error_count += 1
                    self.stdout.write(
                        self.style.ERROR(f"Error importing feedback {item.get('id')}: {str(e)}")
                    )
            
            self.stdout.write(
                self.style.SUCCESS(
                    f"\nImport Summary:\n"
                    f"Successfully imported: {success_count}\n"
                    f"Failed to import: {error_count}"
                )
            )
            
        except FileNotFoundError:
            self.stdout.write(
                self.style.ERROR(f"Could not find file: {file_path}")
            )
        except json.JSONDecodeError as e:
            self.stdout.write(
                self.style.ERROR(f"Invalid JSON file: {str(e)}")
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f"An unexpected error occurred: {str(e)}")
            )