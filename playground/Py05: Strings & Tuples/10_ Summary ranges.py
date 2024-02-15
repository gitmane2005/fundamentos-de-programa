def summary_ranges(a_string):
    number_string = [int(x) for x in a_string.split(",")]
    first = previose = number_string[0]
    result = []
    for i in number_string[1:]:
        if previose + 1 == i:
            previose = i
            continue

        else:
            
            result.append(f"{first}->{previose}" if (previose-first)>=1 else f"{first}" )
            first = previose = i

    result.append(f"{first}->{previose}" if (previose-first)>=1 else f"{first}" )
    

    return ",".join(result)