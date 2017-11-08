def normalize_votes(helpful_ratings):
    """
        in_ : column of dataframe containing tuples of votes
        out_: normalized votes
    """
    
    #compute sum of votes
    sum_of_votes = sum(x[1] for x in helpful_ratings)
    
    #normalize by dividing
    normalized_rating = [x[0]/sum_of_votes for x in helpful_ratings] 
    
    return normalized_rating
