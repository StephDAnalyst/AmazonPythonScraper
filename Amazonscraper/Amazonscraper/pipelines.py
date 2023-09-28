from itemadapter import ItemAdapter
import json

class AmazonscraperPipeline:
    def process_item(self, item, spider):
        
        adapter = ItemAdapter(item)
        price = adapter.get('price', '')

        try:
            if price and price.startswith('$'):
                # Remove the dollar sign and commas
                cleaned_price = price.replace('$', '').replace(',', '')

                # Handle cases where there are no commas
                if '.' in cleaned_price:
                    # Price already in the correct format (e.g., '1234.56')
                    price_value = float(cleaned_price)
                else:
                    # Add a comma to separate dollars and cents, then convert to float
                    price_value = float(cleaned_price[:-2] + '.' + cleaned_price[-2:])

                adapter['price'] = price_value
        except (ValueError, AttributeError):
            adapter['price'] = None

        stars = adapter.get("stars")
        try:
            # Extract the first value before " out of" and convert to float
            float_stars = float(stars.split(" ")[0])
            adapter["stars"] = float_stars
        except (ValueError, AttributeError):
            # If unable to convert or attribute error, set stars to None
            adapter["stars"] = None
        
        rating_count = adapter.get("rating_count")
        try:
            # Extract the first value before " out of" and convert to int
            int_rating_count = int(rating_count.split(" out of")[0])
            adapter["rating_count"] = int_rating_count
        except (ValueError, AttributeError):
            # If unable to convert or attribute error, set rating_count to None
            adapter["rating_count"] = None


        name = adapter.get("name")
        try:
            adapter['name'] = adapter['name'].strip()
        except (ValueError,AttributeError):
            adapter["name"]=None
        
        return item