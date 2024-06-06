# complexity-experiment
Note: Files other than the ones described here might be slightly out of date or confusing as embeddings and participant data and the way they are processed change from time to time.
Important Files:
- Data/Data Prep/get_entropy.ipynb: Calculates entropy from raw entropy scores (each value between 0 and 1)
- Data/Images/HebartRankingImages: Images used in the ranking experiment
- Data/Images/AmbiguousImagesPairs: Images used in the ambiguous experiment
- Final Paper Data/dimensional_complexity_reweighting.ipynb: Processes experiment data and turns it into weights for each dimension
- Final Paper Data/just_weights.csv: Weights for each dimension that can be applied to any image
- Final Paper Data/ambiguous_analysis.ipynb: Reweighting of previously calculated scores for ambiguous entropy scores. Also correlation analysis of participant responses and expected responses based on reweighting.
- Experiments/hebart_ranking_experiment.py: Experiment in which participants were asked to rank 50 images with varying entropy scores by complexity
- Experiments/ambiguous_comparison_experiment.py: Experiment in which participants were asked to compare the complexity of ambiguous images (higher entropy) and their controls (lower entropy)
  
