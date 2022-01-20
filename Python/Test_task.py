# static values for increases and decreases data for 1 day
degrade_value = 2                  
increase_value = 2


def update_quality(item, sell_in, quality, days):
    if item == "Aged Brie":                                     # for Aged Brie item
        item_quality = quality+increase_value*days              # calculation for item quality after 1 day
        if item_quality < 0:                                    # checking item quality is less than 0% or not
            item_quality = 0
        elif item_quality > 50:                                 # checking item quality is greater than 50% or not
            item_quality = 50
        else:
            item_quality = item_quality

    elif item == "Sulfuras":                                    # for Sulfuras item
        item_quality = quality

    elif item == "Backstage passes":                            # for Backstage passes item
        if sell_in <= 5:
            Diff = sell_in - days                               # checking days difference between sell_in and days
            increase_value_Backstage = 3                        # quality increases by 3 when there are 5 days or less    

        elif sell_in <= 10 and sell_in > 5:
            Diff = sell_in - days
            increase_value_Backstage = 2                        # quality increases by 2 when there are 10 days or less

        if Diff == 0:                                           # quality drops to 0 after the concert
            item_quality = 0
        else:
            item_quality = quality+increase_value_Backstage*Diff

        if item_quality < 0:                                            # checking item quality is less than 0% or not
            item_quality = 0
        elif item_quality > 50:                                         # checking item quality is greater than 50% or not
            item_quality = 50
        else:
            item_quality = item_quality

    elif item == "Conjured":                                            # for Conjured item
        if days <= sell_in:
            item_quality = quality-2*(degrade_value*days)               # "Conjured" items degrade in quality twice as fast as normal items
            if item_quality < 0:                                        # checking item quality is less than 0% or not
                item_quality = 0
            elif item_quality > 50:                                     # checking item quality is greater than 50% or not
                item_quality = 50
            else:
                item_quality = item_quality

        else:
            diff = days-sell_in
            item_quality_after = quality-2*(degrade_value*days)-2*(degrade_value*diff)      # Once the sell by date has passed, quality degrades twice as fast 
            if item_quality_after < 0:                                                      # checking item quality is less than 0% or not
                item_quality_after = 0
            elif item_quality_after > 50:                                                   # checking item quality is greater than 50% or not
                item_quality_after = 50
            else:
                item_quality_after = item_quality_after
            return f"After {days} Days Quality is {item_quality_after}%"

    else:                                                                                   # for normal items
        if days <= sell_in:
            item_quality = quality-degrade_value*days                                       # Normal decreases item quality with day
            if item_quality < 0:                                                            # checking item quality is less than 0% or not
                item_quality = 0
            elif item_quality > 50:                                                         # checking item quality is greater than 50% or not
                item_quality = 50
            else:
                item_quality = item_quality

        else:
            diff = days-sell_in
            item_quality_after = quality-degrade_value*days-degrade_value*diff              # Once the sell by date has passed, quality degrades twice as fast 
            if item_quality_after < 0:                                                      # checking item quality is less than 0% or not
                item_quality_after = 0
            elif item_quality_after > 50:                                                   # checking item quality is greater than 50% or not
                item_quality_after = 50
            else:
                item_quality_after = item_quality_after
            return f"After {days} Days Quality is {item_quality_after}%"

    return f"After {days} Days Quality is {item_quality}%"

# inputs
item = "Aged Brie"          # for normal item any value here ex. Abcd
sell_in = 5
quality = 45
days = 7               # how many days gone

print(update_quality(item, sell_in, quality, days))
