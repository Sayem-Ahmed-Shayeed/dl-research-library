# Computer vision

Primary source: `torralba-fcv/` (chapter numbers below are the book's). Code and modern tasks: `zhang-d2l/17-computer-vision.md`.

## Why vision is hard
- Inverse problem: a 2D image is consistent with infinitely many 3D scenes; vision relies on priors (statistics of natural scenes). Read `torralba-fcv/02-1-the-challenge-of-vision.md`, `03-2-a-simple-vision-system.md` (a full hand-built system on a blocks world — great for intuition), `56-55-…revisited.md` (same task with learning).

## Image formation
- Light, reflectance (Lambertian, specular), pinhole camera, lenses (thin-lens equation 1/f = 1/z + 1/z', depth of field, aberrations), sensors, color (trichromacy, color spaces, white balance).
- Cameras as linear systems: image = A · scene; lets you reason about imaging as linear algebra.
- Read: `torralba-fcv/06-5-imaging.md`, `07-6-lenses.md`, `08-7-cameras-as-linear-systems.md`, `09-8-color.md`.

## Linear filtering and signal processing
- Convolution/correlation, separable filters, boundary handling. Gaussian blur (scale), box filter, image derivatives (Sobel, Gaussian derivatives, Laplacian / LoG / DoG).
- Fourier transform: convolution theorem (conv in space = product in frequency), magnitude vs phase (phase carries structure), frequency response of filters.
- Sampling and aliasing: Nyquist; low-pass before downsampling; interpolation when upsampling. CNN striding/pooling also aliases → blur-pooling/anti-aliased CNNs.
- Pyramids: Gaussian (multi-scale), Laplacian (band-pass, blending, compression), steerable pyramids; filter banks (Gabor) model V1 and texture.
- Temporal filters for video and motion.
- Read: `torralba-fcv/16-15-…` through `24-23-image-pyramids.md`, `20-19-temporal-filters.md`.

## Statistical image models and perceptual organization
- Natural image statistics: 1/f power spectrum, heavy-tailed (sparse) derivative distributions → priors for denoising/deblurring.
- Texture: Julesz, Portilla–Simoncelli statistics, Gram-matrix texture synthesis / style transfer.
- MRFs / graphical models on pixels (denoising, segmentation, stereo). Perceptual grouping: Gestalt, segmentation, contours.
- Read: `torralba-fcv/28-27-statistical-image-models.md`, `29-28-textures.md`, `30-29-probabilistic-graphical-models.md`, `32-31-perceptual-grouping.md`; `bishop-prml/10-8-graphical-models.md` §8.3 (image denoising MRF).

## Geometry
- Homogeneous coordinates; 2D transforms hierarchy: translation ⊂ Euclidean ⊂ similarity ⊂ affine ⊂ projective (homography, 8 DOF, estimated by DLT from ≥4 points + RANSAC).
- Camera model x = K[R|t]X; intrinsics K (focal length, principal point), extrinsics R,t; calibration (Zhang's checkerboard), lens distortion.
- Single-view metrology: vanishing points/lines, measuring heights from one image.
- Stereo: epipolar geometry, fundamental matrix F (x'ᵀFx = 0), essential matrix E = [t]ₓR, rectification, disparity d ⇒ depth Z = fB/d, matching cost + regularization.
- Structure from motion: feature matching (SIFT-like), triangulation, bundle adjustment (nonlinear least squares over cameras and points).
- Monocular depth learning; radiance fields (NeRF: MLP σ, c(x, d) + volume rendering C = Σ Tᵢ(1−e^{−σᵢδᵢ})cᵢ; 3D Gaussian splatting as faster successor); 3D learning on point clouds/voxels/meshes.
- Read: `torralba-fcv/39-38-…` through `46-45-radiance-fields.md`, and `44-43-learning-to-estimate-depth-from-a-single-image.md`.

## Motion
- Motion field vs optical flow; brightness constancy Iₓu + I_yv + I_t = 0 (aperture problem); Lucas–Kanade (local least squares), Horn–Schunck (global smoothness); coarse-to-fine pyramids.
- 3D motion projected to 2D (focus of expansion, ego-motion); learned flow (FlowNet, RAFT-style correlation volumes + iterative refinement), self-supervised flow via photometric loss.
- Read: `torralba-fcv/47-46-…`, `48-47-…`, `49-48-optical-flow-estimation.md`, `50-49-learning-to-estimate-motion.md`.

## Recognition and dense prediction
- Classification: ImageNet, top-1/top-5; transfer of pretrained backbones.
- Detection: two-stage (R-CNN → Fast → Faster R-CNN with RPN + anchors), one-stage (SSD, YOLO, RetinaNet with focal loss), anchor-free (FCOS/CenterNet), set prediction transformers (DETR, Hungarian matching). IoU, NMS, mAP@[.5:.95].
- Segmentation: semantic (FCN, U-Net, DeepLab with atrous conv), instance (Mask R-CNN), panoptic, promptable (SAM-style). Metric mIoU.
- Read: `torralba-fcv/51-50-object-recognition.md`; `zhang-d2l/17-computer-vision.md` (augmentation, fine-tuning, anchors, SSD, R-CNNs, FCN, style transfer, Kaggle examples); `murphy-pml1/15-14-neural-networks-for-images.md`.

## Representation learning for vision
- Supervised pretraining → self-supervised: contrastive (SimCLR, MoCo; InfoNCE), non-contrastive (BYOL, DINO), masked image modeling (MAE), CLIP (image–text contrastive).
- Generative models as representation learners and vice versa.
- Read: `torralba-fcv/31-30-representation-learning.md`, `34-33-generative-modeling-meets-representation-learning.md`; `murphy-pml2/33-32-representation-learning.md`.

## Vision and language
- Joint embeddings (CLIP), captioning, VQA, text-to-image generation, VLMs (vision encoder + projector + LLM).
- Read: `torralba-fcv/52-51-vision-and-language.md`; `torralba-fcv/35-34-conditional-generative-models.md`.

## Robustness, bias, ethics
- Dataset bias ("name that dataset"), distribution shift (covariate, label), adversarial examples, domain adaptation, test-time adaptation, fairness and societal impact.
- Read: `torralba-fcv/36-35-data-bias-and-shift.md`, `37-36-training-for-robustness-and-generality.md`, `38-37-transfer-learning-and-adaptation.md`, `05-4-computer-vision-and-society.md`; `murphy-pml2/20-19-beyond-the-iid-assumption.md`; `prince-udl/22-deep-learning-and-ethics.md`.

## Classical-to-deep cheat sheet
| Classical | Deep counterpart |
|---|---|
| Gabor/filter banks | First-layer CNN filters |
| Image pyramids | FPN, U-Net multi-scale |
| SIFT/HOG + SVM | CNN features + linear head |
| MRF/CRF smoothing | CRF-as-RNN, learned refinement |
| Block matching stereo | Cost volumes + 3D conv |
| Lucas–Kanade | RAFT-style iterative refinement |
| Bundle adjustment | Differentiable BA, learned SfM |
| Texture statistics | Gram matrices, style transfer |
