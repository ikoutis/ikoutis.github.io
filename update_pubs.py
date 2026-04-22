import re

html_content = '''                    <li class="publication-item">
                        <div class="publication-title">Scalable Constrained Clustering: A Generalized Spectral Method</div>
                        <div class="publication-authors"><strong>I. Koutis</strong>, M. Cucuringu, S. Chawla, G. Miller, R. Peng</div>
                        <div class="publication-venue">AISTATS 2016</div>
                        <div class="publication-links">
                            <a href="https://arxiv.org/abs/1601.04746" class="tag" target="_blank">arXiv</a>
                        </div>
                    </li>
                    <li class="publication-item">
                        <div class="publication-title">Spanning Edge Centrality: Large-scale computations and applications</div>
                        <div class="publication-authors"><strong>I. Koutis</strong>, C. Mavroforakis, R. Garcia-Lebron, E. Terzi</div>
                        <div class="publication-venue">WWW 2015</div>
                        <div class="publication-links">
                            <a href="./papers/spanning_edge.pdf" class="tag" target="_blank">PDF</a>
                        </div>
                    </li>
                    <li class="publication-item">
                        <div class="publication-title">Simple parallel and distributed algorithms for spectral graph sparsification</div>
                        <div class="publication-authors"><strong>I. Koutis</strong></div>
                        <div class="publication-venue">SPAA 2014</div>
                        <div class="publication-links">
                            <a href="https://arxiv.org/abs/1402.3851" class="tag" target="_blank">arXiv</a>
                        </div>
                    </li>
                    <li class="publication-item">
                        <div class="publication-title">A fast solver for a class of linear systems</div>
                        <div class="publication-authors"><strong>I. Koutis</strong>, G. Miller, R. Peng</div>
                        <div class="publication-venue">Communications of the ACM</div>
                        <div class="publication-links">
                            <a href="./papers/CACM-KMP.pdf" class="tag" target="_blank">PDF</a>
                        </div>
                    </li>
                    <li class="publication-item">
                        <div class="publication-title">Faster spectral sparsification and numerical algorithms for SDD matrices</div>
                        <div class="publication-authors"><strong>I. Koutis</strong>, A. Levin, R. Peng</div>
                        <div class="publication-venue">STACS 2012</div>
                        <div class="publication-links">
                            <a href="https://arxiv.org/abs/1209.5821" class="tag" target="_blank">arXiv</a>
                            <a href="./papers/stacs239koutis.pdf" class="tag" target="_blank">PDF</a>
                        </div>
                    </li>
                    <li class="publication-item">
                        <div class="publication-title">Constrained multilinear detection for faster functional motif discovery</div>
                        <div class="publication-authors"><strong>I. Koutis</strong></div>
                        <div class="publication-venue">Information Processing Letters 2012</div>
                        <div class="publication-links">
                            <a href="https://arxiv.org/abs/1206.3483" class="tag" target="_blank">arXiv</a>
                        </div>
                    </li>
                    <li class="publication-item">
                        <div class="publication-title">Train marshalling is fixed parameter tractable</div>
                        <div class="publication-authors"><strong>I. Koutis</strong>, L. Brueggeman, M. Fellows, R. Fleischer, M. Lackner, C. Komusiewicz, A. Pfandler, F. Rosamond</div>
                        <div class="publication-venue">FUN 2012</div>
                        <div class="publication-links">
                            <a href="./papers/fun2012.pdf" class="tag" target="_blank">PDF</a>
                        </div>
                    </li>
                    <li class="publication-item">
                        <div class="publication-title">A nearly-m*logn solver for SDD linear systems</div>
                        <div class="publication-authors"><strong>I. Koutis</strong>, G. Miller, R. Peng</div>
                        <div class="publication-venue">FOCS 2011</div>
                        <div class="publication-links">
                            <a href="https://arxiv.org/abs/1102.4842" class="tag" target="_blank">arXiv</a>
                        </div>
                    </li>
                    <li class="publication-item">
                        <div class="publication-title">Combinatorial preconditioners and multilevel solvers for problems in computer vision and image processing</div>
                        <div class="publication-authors"><strong>I. Koutis</strong>, G. Miller, D. Tolliver</div>
                        <div class="publication-venue">Computer Vision and Image Understanding 2011 / ISVC 2009</div>
                        <div class="publication-links">
                            <a href="./papers/cviu_preprint.pdf" class="tag" target="_blank">PDF</a>
                            <a href="./papers/isvc-main.pdf" class="tag" target="_blank">Conference PDF</a>
                        </div>
                    </li>
                    <li class="publication-item">
                        <div class="publication-title">Near linear-work parallel SDD solvers, low-diameter decomposition and low-stretch subgraphs</div>
                        <div class="publication-authors"><strong>I. Koutis</strong>, G. Blelloch, A. Gupta, G. Miller, R. Peng, K. Tangwongsan</div>
                        <div class="publication-venue">SPAA 2011</div>
                        <div class="publication-links">
                            <a href="./papers/SPAA11.pdf" class="tag" target="_blank">PDF</a>
                        </div>
                    </li>
                    <li class="publication-item">
                        <div class="publication-title">Spectral counting of triangles in power-law networks via element-wise sparsification and triangle-based link recommendation</div>
                        <div class="publication-authors"><strong>I. Koutis</strong>, C. Tsourakakis, P. Drineas, E. Michelakis, C. Faloutsos</div>
                        <div class="publication-venue">Social Network Analysis and Mining / ASONAM 2009</div>
                        <div class="publication-links">
                            <a href="./papers/SNAM_2011.pdf" class="tag" target="_blank">PDF</a>
                            <a href="./papers/ASONAM09.pdf" class="tag" target="_blank">Conference PDF</a>
                        </div>
                    </li>
                    <li class="publication-item">
                        <div class="publication-title">Approaching optimality for solving SDD systems</div>
                        <div class="publication-authors"><strong>I. Koutis</strong>, G. Miller, R. Peng</div>
                        <div class="publication-venue">FOCS 2010</div>
                        <div class="publication-links">
                            <a href="https://arxiv.org/abs/1003.2958" class="tag" target="_blank">arXiv</a>
                        </div>
                    </li>
                    <li class="publication-item">
                        <div class="publication-title">Hierarchical Diagonal Blocking with precision reduction applied to combinatorial multigrid</div>
                        <div class="publication-authors"><strong>I. Koutis</strong>, G. E. Blelloch, G. Miller, K. Tangwongsan</div>
                        <div class="publication-venue">SC10</div>
                        <div class="publication-links">
                            <a href="./papers/SC10-paper.pdf" class="tag" target="_blank">PDF</a>
                        </div>
                    </li>
                    <li class="publication-item">
                        <div class="publication-title">Limits and applications of group algebras for parameterized problems</div>
                        <div class="publication-authors"><strong>I. Koutis</strong>, R. Williams</div>
                        <div class="publication-venue">ICALP 2009</div>
                        <div class="publication-links">
                            <a href="./papers/KW-full.pdf" class="tag" target="_blank">PDF</a>
                            <a href="./papers/icalp09.pdf" class="tag" target="_blank">Original PDF</a>
                        </div>
                    </li>
                    <li class="publication-item">
                        <div class="publication-title">Faster algebraic algorithms for path and packing problems</div>
                        <div class="publication-authors"><strong>I. Koutis</strong></div>
                        <div class="publication-venue">ICALP 2008</div>
                        <div class="publication-links">
                            <a href="./papers/MultilinearDetection.pdf" class="tag" target="_blank">PDF</a>
                        </div>
                    </li>
                    <li class="publication-item">
                        <div class="publication-title">Graph partitioning into isolated, high conductance clusters: theory, computation and applications to preconditioning</div>
                        <div class="publication-authors"><strong>I. Koutis</strong>, G. Miller</div>
                        <div class="publication-venue">SPAA 2008</div>
                        <div class="publication-links">
                            <a href="./papers/multiwayedge.pdf" class="tag" target="_blank">PDF</a>
                        </div>
                    </li>
                    <li class="publication-item">
                        <div class="publication-title">Unassisted Segmentation of Multiple Retinal Layers via Spectral Rounding</div>
                        <div class="publication-authors"><strong>I. Koutis</strong>, D. Tolliver, H. Ishikawa, J. Shuman, G. Miller</div>
                        <div class="publication-venue">ARVO 2008</div>
                        <div class="publication-links">
                            <a href="http://www.cs.cmu.edu/~glmiller/Publications/TKISM-ARVO2008.pdf" class="tag" target="_blank">PDF</a>
                        </div>
                    </li>
                    <li class="publication-item">
                        <div class="publication-title">Combinatorial and algebraic tools for optimal multilevel algorithms</div>
                        <div class="publication-authors"><strong>I. Koutis</strong></div>
                        <div class="publication-venue">PhD Thesis, CMU-CS-07-131</div>
                        <div class="publication-links">
                            <a href="./papers/main.pdf" class="tag" target="_blank">PDF</a>
                        </div>
                    </li>
                    <li class="publication-item">
                        <div class="publication-title">A linear work O(n<sup>1/6</sup>) time algorithm for solving planar Laplacians</div>
                        <div class="publication-authors"><strong>I. Koutis</strong>, G. Miller</div>
                        <div class="publication-venue">SODA 2007</div>
                        <div class="publication-links">
                            <a href="./papers/planar.pdf" class="tag" target="_blank">PDF</a>
                        </div>
                    </li>
                    <li class="publication-item">
                        <div class="publication-title">Parameterized complexity and improved inapproximability for computing the largest j-simplex in a V-polytope</div>
                        <div class="publication-authors"><strong>I. Koutis</strong></div>
                        <div class="publication-venue">Information Processing Letters 2006</div>
                        <div class="publication-links">
                            <a href="./papers/Vpolytopes.pdf" class="tag" target="_blank">PDF</a>
                        </div>
                    </li>
                    <li class="publication-item">
                        <div class="publication-title">Dimensionality restrictions on sums over Z<sub>p</sub><sup>d</sup></div>
                        <div class="publication-authors"><strong>I. Koutis</strong></div>
                        <div class="publication-venue">Technical Report CMU-CS-07-103</div>
                        <div class="publication-links">
                            <a href="./papers/zero.pdf" class="tag" target="_blank">PDF</a>
                            <a href="./papers/ggzs.pdf" class="tag" target="_blank">Related PDF</a>
                        </div>
                    </li>
                    <li class="publication-item">
                        <div class="publication-title">A faster parameterized algorithm for set packing</div>
                        <div class="publication-authors"><strong>I. Koutis</strong></div>
                        <div class="publication-venue">Information Processing Letters 2005</div>
                        <div class="publication-links">
                            <a href="./papers/SetPacking.pdf" class="tag" target="_blank">PDF</a>
                        </div>
                    </li>
                    <li class="publication-item">
                        <div class="publication-title">On the hardness of approximate multivariate integration</div>
                        <div class="publication-authors"><strong>I. Koutis</strong></div>
                        <div class="publication-venue">APPROX 2003</div>
                        <div class="publication-links">
                            <a href="./papers/integrate_inapprox.pdf" class="tag" target="_blank">PDF</a>
                        </div>
                    </li>
                    <li class="publication-item">
                        <div class="publication-title">Parallel computation of matrix pseudospectra: a case for load balancing</div>
                        <div class="publication-authors"><strong>I. Koutis</strong>, C. Bekas, E. Gallopoulos, E. Kokiopoulou</div>
                        <div class="publication-venue">ICS 2001</div>
                        <div class="publication-links">
                            <a href="./papers/balancing.pdf" class="tag" target="_blank">PDF</a>
                        </div>
                    </li>
                    <li class="publication-item">
                        <div class="publication-title">Spectrum through pseudospectrum</div>
                        <div class="publication-authors"><strong>I. Koutis</strong>, E. Gallopoulos</div>
                        <div class="publication-venue">FOCM 1999</div>
                        <div class="publication-links">
                            <a href="https://arxiv.org/abs/math/0701368" class="tag" target="_blank">arXiv</a>
                        </div>
                    </li>
                    <li class="publication-item">
                        <div class="publication-title">Exclusion regions and fast estimation of pseudospectra</div>
                        <div class="publication-authors"><strong>I. Koutis</strong></div>
                        <div class="publication-venue">2003 SIAM annual meeting</div>
                        <div class="publication-links">
                            <a href="./papers/excl_ps.pdf" class="tag" target="_blank">PDF</a>
                        </div>
                    </li>'''

with open('publications.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<!-- Older publications have been abridged here for brevity, keeping the most relevant format. -->', html_content)

with open('publications.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done!')
