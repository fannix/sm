n = 50
tweet_per_day = rpois(n, 5)

ground_truth = rep(0, n)
predicted = rep(0, n)

for (i in  1:n){
    sample_size = tweet_per_day[i]
    sample <- rmultinom(1, size = sample_size, prob=c(0.3,0.4,0.3))
    ground_truth[i] <- -sample[1] + sample[3]

    #flip
    keep_rate <- 0.9
    flip_rate <- (1 - keep_rate) / 2
    predicted_value <- 0
    for (j in rep(1, sample[1])){
        new_sample <- rmultinom(1, 1, prob=c(keep_rate, flip_rate, flip_rate)) 
        predicted_value <- predicted_value - new_sample[1] + new_sample[3]
    }
    for (j in rep(1, sample[2])){
        new_sample <- rmultinom(1, 1, prob=c(flip_rate, keep_rate, flip_rate)) 
        predicted_value <- predicted_value - new_sample[1] + new_sample[3]
    }
    for (j in rep(1, sample[3])){
        new_sample <- rmultinom(1, 1, prob=c(flip_rate, flip_rate, keep_rate)) 
        predicted_value <- predicted_value - new_sample[1] + new_sample[3]
    }
    predicted[i] <- predicted_value
}


ground_truth
predicted
sum(sign(ground_truth) == sign(predicted))
